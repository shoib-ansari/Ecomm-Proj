
function check_coupon_code(temp) {
  alert("i am called")
  coupon_code_by_user = $('#coupon_field').val()
  $.ajax({
    url: "/offers/check_coupon",
    method: 'get',
    data: {
      'user_input': coupon_code_by_user,
      'data': temp
    },
    beforeSend: function () {
      // alert("applying")
      if (document.contains(document.getElementById("inv_mess"))) {
        document.getElementById("inv_mess").remove();
      }
    },
    success: function (data) {
      data = data.split(",")
      if (temp == 'a') {
        alert("hello remove is a")
        if (data[1] == 'invalid') {
          // $('.messaged').html('<div class="message"> Invalid coupon code </div>')
          // setTimeout(function () { $('.messaged').empty() }, 2000);
          message = document.createElement('p');
          message.setAttribute("id", "inv_mess");
          message.innerHTML = "Invalid Coupon Code !"
          document.getElementById('coupon_div').appendChild(message)
          $('#coupon_rmv_btn').hide()
        }
        else {
          alert("applied")
          message = document.createElement('p');
          message.setAttribute("id", "inv_mess");
          message.innerHTML = " Applied !"
          message.style.color = 'green'
          document.getElementById('coupon_div').appendChild(message)
          $('#coupon_apl_btn').hide()
          $('#coupon_rmv_btn').show()
          return false
        }
      }
      else {
        message = document.createElement('p');
        message.setAttribute("id", "inv_mess");
        message.innerHTML = " Removed !"
        message.style.color = 'yellow'
        document.getElementById('coupon_div').appendChild(message)
        $('#coupon_apl_btn').show()
        $('#coupon_rmv_btn').hide()
      }
    }
  })
}

$('#coupon_field').on('input', function (e) {
  $('#coupon_apl_btn').html("Apply code")
  $('#coupon_apl_btn').addClass("btn-outline-primary");
  $('#coupon_apl_btn').removeClass("btn-primary");
  // $('#coupon_apl_btn').
});
function apply_coupn(e) {
  min_transaction = parseInt(e.getAttribute('min'))
  code = e.getAttribute('code')
  amt = parseInt(document.getElementById("ttl_amt").innerHTML);
  if (amt >= min_transaction) {
    $.ajax({
      url: "/offers/apply_coupen",
      method: 'get',
      data: {
        'code': code,
      },
      beforeSend: function () {
        if (document.contains(document.getElementById("inv_mess"))) {
          document.getElementById("inv_mess").remove();
        }
      },
      success: function (data) {
        data = data.split(",")
        $('#coupon_field').val(data[0])
        message = document.createElement('p');
        message.setAttribute("id", "inv_mess");
        message.innerHTML = " Applied !"
        message.style.color = 'green'
        document.getElementById('coupon_div').appendChild(message)
        $('#coupon_apl_btn').hide()
         $('#coupon_rmv_btn').show()
        //  $('#coupon_field').val('')
      }
    })
  }
  else {
    $('.messaged').html('<div class="message">Your Cart value must be greter than min. transaction </div>')
    setTimeout(function () { $('.messaged').empty() }, 2000);
  }
}
function remove_prod(e) {
  cart_prod_id = e.getAttribute('c_id')
  temp_id = "clr_" + cart_prod_id
  qty_pr_ele = document.getElementById(temp_id)
  var p = parseInt(qty_pr_ele.getAttribute('p'))
  var q = parseInt(qty_pr_ele.getAttribute('q'))
  alert(p + "____" + q)
  e.parentNode.parentNode.removeChild(e.parentNode);
  $.ajax({
    url: '/cart/remove_prod_from_cart',
    type: 'get',
    data: {
      'cart_prod_id': cart_prod_id
    },
    beforeSend: function () {
      // $('#loading_area').show();
      var amt = document.getElementById("ttl_amt").innerHTML;
      alert(amt)
      amt = amt - (p * q)
      alert("amount after" + amt)
      $('#ttl_amt').html(amt)
    },
  })
}
function update_qty(ele, temp) {
  $.ajax({
    url: '/cart/update_cart',
    type: 'get',
    data: {
      'id': ele.getAttribute('clr_id'),
      'data': temp
    },
    beforeSend: function () {
      $('#loading_area').show();
      $("#inv_mess").remove();
    },
    success: function (data) {
      qty = 0;
      amt = 0;
      $('#loading_area').hide();
      var arr = data.split("?")
      // If product remain in cart (i.e.., qty is more than 0)
      var amt = document.getElementById("ttl_amt").innerHTML;
      if (arr[2] == 'Y') {
        var target_id = "qty_of_" + arr[0]
        var qty = document.getElementById(target_id).value;
        if (temp == 'up') {
          amt = parseInt(amt) + parseInt(arr[1])
          qty++;
        }
        else {
          amt = parseInt(amt) - parseInt(arr[1])
          qty--;
        }
        document.getElementById(target_id).value = qty;
        // update amount
        $('#ttl_amt').html(amt)
      }
      //  product deleted from the cart (i.e.., qty is 0)
      else {
        target_id = "p_c_" + arr[0]
        document.getElementById(target_id).remove()
        amt = parseInt(amt) - parseInt(arr[1])
        $('#ttl_amt').html(amt)
      }
      $('.number').html(parseInt(arr[3]))
      if (arr[4] == 'remove') {
        $coupon_btn = $('#coupon_apl_btn')
        $coupon_btn.html("Apply code")
        $coupon_btn.addClass("btn-outline-primary");
        $coupon_btn.removeClass("btn-primary");
        $('#coupon_field').val('')
      }
    }
  })
}