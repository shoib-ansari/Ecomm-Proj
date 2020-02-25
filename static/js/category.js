

    
    $(document).ready(function () {
        var url = window.location.href
        cats = url.split("/")
        var cat_id = cats[6]
        cat_id = parseInt(cat_id)
        if ((url).endsWith("change/")){
            $.ajax({
                url : '/products/getsubcat',
                type: 'get',
                data: {
                  'cat_id': cat_id
                },
                beforeSend: function () {
                },
                success: function(data){
                    var ct_list =[]
                    for(i=0;i<data.length;i++){
                        ct_list.push(data[i].toString())
                    }
                    // console.log(ct_list)

                    $("select[name*='finalcategory_set-'][name$=sub_category]").each(function (i, el) {
                        // console.log(el)
                        for (j = 1; j < el.options.length; j++) {
                           console.log(el.options[j].value)
                           if(! ct_list.includes(el.options[j].value)){
                            $("option[value="+el.options[j].value+"]").remove(); 

                           }
                        }
                    });
                }
            })
        }
    });