$(document).ready(function () {
     // Variables inetialized to set value erased in sub and final cat
    var sub_cat_val = 0
    var final_cat_val = 0
    counter = 0
    // Counter used b/c onchange event of main categories triggered automatically after page load
       

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
                            break;
                        }
                    }
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
                    if(sub_cat_val !== i || counter!==1){
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
        counter++;

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


    sel = document.getElementById('id_tags')
    field = document.getElementsByClassName('field-tags')[0]
    field.innerHTML = ''
    disp_row = document.createElement('div')
    disp_row.classList.add('form-row')
    // disp_row.innerHTML = 'Hello'
    field.appendChild(disp_row)
    row = document.createElement('row')
    // label = document.createElement('label')
    // label.setAttribute("for","id_tags")
    inp = document.createElement('input')
    inp.type = 'select';
    data_list = document.createElement('datalist')
    data_list.setAttribute('id','tag_list')
    inp.setAttribute('list',"tag_list")
    inp.classList.add('vTextField')
    inp.placeholder = "Type a tag and hit enter.";
    inp.setAttribute('id','sel_temp')
    row.appendChild(inp)
    row.appendChild(data_list)
    field.appendChild(row)
    sel.remove()
    var opts = [], opt;

    inp.onkeypress = KeyPressHandler;
    function KeyPressHandler(event){
     // create a chip ui when user press enter
  if (event.keyCode === 13 && inp.value.length>0  ) {
        event.preventDefault();
          tag_item = document.createElement('span')
          tag =inp.val
          tag_item.innerHTML = inp.value
          tag_item.setAttribute('id',inp.value)
          tag_item.setAttribute('tag_text',inp.value)
          tag_item.classList.add('chip')
        //   console.log(tag_item)
          remove = document.createElement('span')
          remove.innerHTML = 'x'
          remove.setAttribute('tag_id',inp.value)
          remove.addEventListener('click', remove_tag);
          remove.classList.add('rem_btn')
          tag_item.appendChild(remove)
          disp_row.appendChild(tag_item)
        //   console.log(tag_item)
          inp.value = ''
        }
  return !(window.event && window.event.keyCode == 13);
}



// Function to get data for tags as suggestions
document.getElementById('sel_temp').onkeyup = function(){
     ent_data = document.getElementById('sel_temp').value

    var tag_data = new XMLHttpRequest();
        tag_data.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var data = (this.responseText)
                data = JSON.parse(data)
                // alert(data.length)
                data_list = document.getElementById('tag_list')
                data_list.innerHTML = ''
                for(var i = 0; i<data.length;i++){
                    // console.log("creating")
                    option = document.createElement('option')
                    option.value = data[i]['name']
                    option.setAttribute('t_id',data[i]['id'])
                    data_list.appendChild(option)
                }
            }
        };

        tag_data.open("GET", "/products/get_tag_data/" + ent_data, true);
        tag_data.send();
};

    // loop through options in select list
    for (var i=0, len=sel.options.length; i<len; i++) {
        opt = sel.options[i];
        if ( opt.selected ) {
            opts.push(opt.value);
        }}

        // Create select box when user submits
        document.getElementById('product_form').addEventListener("submit", function(e){check_tags(e)});

        function check_tags(e) {
            e.preventDefault();
            tags = []
            var tags_comp = document.getElementsByClassName('chip')
            for(var i=0; i<tags_comp.length;i++){
                tags.push(tags_comp[i].getAttribute('tag_text'))
            }
            var check_tag_data = new XMLHttpRequest();
            check_tag_data.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var data = (this.responseText)
                    data = JSON.parse(data)
                    var sel = document.createElement('select')
                    sel.name = 'tags'
                    sel.setAttribute('id','id_tags')
                    sel.multiple = true;
                    for(var i=0; i<data.length; i++){
                        var option = document.createElement("option");
                        option.selected = true;
                        option.value = data[i]['id']
                        sel.add(option)
                    }
                    for (var i=0; i<sel.options.length; i++) {
                        sel.options[i].selected = true;
                        }
                    document.getElementById('product_form').appendChild(sel)
                    console.log(sel)
                    document.getElementById('product_form').submit();
                }
                
            };
            check_tag_data.open("GET", "/products/check_tag_data/" + tags , true);
            check_tag_data.send();
        }

get_curr_tags();

function get_curr_tags() {
    
        if((window.location.href).indexOf('change') !== -1){
            // alert(window.location.href)
            var get_tags = new XMLHttpRequest();
            get_tags.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    data = this.responseText
                    data = JSON.parse(data)
                    for(var i=0;i<data.length;i++){
                        tag_item = document.createElement('span')
                        tag =inp.val
                        tag_item.innerHTML = data[i]['name']
                        tag_item.setAttribute('id',data[i]['name'])
                        tag_item.setAttribute('tag_text',data[i]['name'])
                        tag_item.classList.add('chip')
                        remove = document.createElement('span')
                        remove.innerHTML = 'x'
                        remove.setAttribute('tag_id',data[i]['name'])
                        remove.addEventListener('click', remove_tag);
                        remove.classList.add('rem_btn')
                        tag_item.appendChild(remove)
                        disp_row.appendChild(tag_item)
                    }
                 
            }
        };

            get_tags.open("GET", "/products/get_tags/" + window.location.href , true);
            get_tags.send();
    }
        
       

    }

    function remove_tag(e) {
        console.log("Clicked " + this.getAttribute('tag_id'));
        temp_id = this.getAttribute('tag_id')
        document.getElementById(temp_id).remove();
    }
});