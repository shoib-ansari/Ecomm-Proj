$(document).ready(function () {
    category = $('#id_name').val();
    $test = $('select[id ^=id_finalcategory][id $=category]')
    $test.each(function (a) {
        console.log($(this))
        $id = ($(this).attr('id'))
        alert(('$(this) option:contains("Selection 1")'))
        var option_name = $(this).find('*');
        // option_name.remove('*')
    });
    $.ajax({
        url: '/products/getsubcat',
        type: 'get',
        data: {
            category: category
        },
        success: function (data) {
            alert(data)
            var temp = data.split("%");
            var id = []
            var name = []

            for (i = 0; i < temp.length; i++) {
                var temp2 = temp[i].split("^")
                id.push(temp2[0])
                name.push(temp2[1])
            }
            $test.each(function () {
                for (i = 0; i < id.length; i++) {
                    $(this)
                        .append($("<option></option>")
                            .attr("value", id[i])
                            .text(name[i]));
                }
            });
},
    failure: function (data) {
        alert('Got an error dude');
    }
    });
});