$(document).ready(function () {
    var sub_cat_val = 0
    var final_cat_val = 0
        // JS to set value erased

        var url = window.location.href
        if ((url).endsWith("change/")) {
            temp = url.split("/")
            p_id = temp[temp.length - 3]
            // alert(p_id)
            var values_data = new XMLHttpRequest();
            values_data.open("GET", "/products/get_cat_data?" + p_id, true);
            values_data.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var data = this.responseText
                    data = data.split("~")
                    // alert(data[1])
                    console.log(this.responseText)
                    // 
                    var x = document.getElementById("id_sub_category");
                    for (i = 0; i < x.options.length; i++) {
                        if(x.options[i].text == data[1]) {
                            sub_cat_val = i
                            // document.getElementById("id_sub_category").selectedIndex = i;
                            break;
                        }
                    }
                    // var y = document.getElementById("id_Final_category");
                    final_cat_val= data[3]
                }
            };
            values_data.send();
        }




    var main_Cat = document.getElementById("id_Main_category")
    var sub_Cat = document.getElementById("id_sub_category")
    main_Cat.onchange = function () {
        var selectedvalue = main_Cat.value;
        var main_cat_obj = new XMLHttpRequest();
        main_cat_obj.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var temp = (this.responseText).split("%");
                var id = []
                var name = []
                for (i = 0; i < temp.length; i++) {
                    var temp2 = temp[i].split("^")
                    id.push(temp2[0])
                    name.push(temp2[1])
                }
                var sel = document.getElementById("id_sub_category");
                for (i = sel.length - 1; i >= 1; i--) {
                    if(sub_cat_val !== i){
                        sel.remove(i);
                    }
                }
                var sel = document.getElementById("id_Final_category");
                for (i = sel.length - 1; i >= 1; i--) {
                    sel.remove(i);
                }
                for (i = 0; i < id.length; i++) {
                    
                        // get reference to select element
                    var sel = document.getElementById('id_sub_category');
                    // create new option element
                    var opt = document.createElement('option');
                    // create text node to add to option element (opt)
                    opt.appendChild(document.createTextNode(name[i]));
                    // set value property of opt
                    opt.value = id[i];
                    // add opt to end of select box (sel)
                    sel.appendChild(opt);
                    if(opt.text == final_cat_val){
                        opt.selected = 'true';
                    }
                }
            }
        };
        main_cat_obj.open("GET", "/products/getsubcategories/" + selectedvalue, true);
        main_cat_obj.send();
    }

    sub_Cat.onchange = function () {
        var selectedsubcat = sub_Cat.value
        // ajax starts 
        var sub_cat_obj = new XMLHttpRequest();
        sub_cat_obj.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var temp = (this.responseText).split("%");
                var id = []
                var name = []

                for (i = 0; i < temp.length; i++) {
                    var temp2 = temp[i].split("^")
                    id.push(temp2[0])
                    name.push(temp2[1])
                }
                var sel = document.getElementById("id_Final_category");
                for (i = sel.length - 1; i >= 1; i--) {
                    sel.remove(i);
                }
                for (i = 0; i < id.length; i++) {
                    // get reference to select element
                    var sel = document.getElementById('id_Final_category');
                    // create new option element
                    var opt = document.createElement('option');
                    // create text node to add to option element (opt)
                    opt.appendChild(document.createTextNode(name[i]));
                    // set value property of opt
                    opt.value = id[i];
                    // add opt to end of select box (sel)
                    sel.appendChild(opt);
                    if(opt.text == final_cat_val){
                        opt.selected = 'true';
                    }
                }
                
            }
        };

        sub_cat_obj.open("GET", "/products/getfinalcategories/" + selectedsubcat, true);
        sub_cat_obj.send();
    }
    var add_final_cat = document.querySelectorAll('[id^=id_finalcategory_set-]')
    add_final_cat.onchange = function () {
    }




});