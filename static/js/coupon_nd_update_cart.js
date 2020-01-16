
$('#coupon_field').on('input', function (e) {
  $('#coupon_apl_btn').html("Apply code")
  $('#coupon_apl_btn').addClass("btn-outline-primary");
  $('#coupon_apl_btn').removeClass("btn-primary");
  // $('#coupon_apl_btn').
});
function rmv_coupon(){
  $.ajax({
    url:'/offers/rmv_coupon',
    beforeSend: function(){
      alert('removing')
    },
    success:function(data){
      alert("removed")
      $('#coupon_field').val('')
      // Displaying removed message
      if (document.contains(document.getElementById("inv_mess"))) {
        document.getElementById("inv_mess").remove();
      } 
      message = document.createElement('p');
      message.setAttribute("id", "inv_mess");
      message.innerHTML = " Removed !"
      message.style.color = 'Brown'
      document.getElementById('coupon_div').appendChild(message)
      $('#coupon_apl_btn').hide()
      $('#coupon_rmv_btn').show()
        $('#cb').empty();
      $('#coupon_rmv_btn').hide()
      $('#f_amt').text(data)
    }
  })
}



// Function to apply coupon code on click on apply button
function apply_coupn(e) {
  min_transaction = parseInt(e.getAttribute('min'))
  code = e.getAttribute('code')
  amt = parseInt(document.getElementById("ttl_amt").innerHTML);
  // If Coupon code is valid for cart
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
        if (data[1] == 'invalid cart amount') {
          // When user is using two much of his/her brain....
          message = document.createElement('p');
          message.setAttribute("id", "inv_mess");
          message.innerHTML = "Zada dimag laga rha h ?? tu khud hi kr le apne aap. Ruk teri id block krta hu abhi !"
          document.getElementById('coupon_div').appendChild(message)
          $('#coupon_field').val('')
        }
        else {
        // -----------  <<< Creating 'applied' message  >>> --------
          $('#coupon_field').val(data[0])
          message = document.createElement('p');
          message.setAttribute("id", "inv_mess");
          message.innerHTML = " Applied !"
          message.style.color = 'green'
          document.getElementById('coupon_div').appendChild(message)
          $('#coupon_rmv_btn').show()
          // col_div = document.createElement('div')
          // col_div.className += 'col-md-6'
          $('#cb').html('<div class="col-md-6 text-success">Cashback</div><div class="col-md-6 text-right" id="cb_price"></div>')
          $("#cb_price").text(data[1])
          $('#f_amt').text(data[2])
          $('#coupon_rmv_btn').show()
        }
      }
    })
  }
  // If coupon code is not valid for cart
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


function update_qty(ele,temp) {
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
        // ---------- <<<  Creating coupon code Removed Message
        message = document.createElement('p');
        message.setAttribute("id", "inv_mess");
        message.innerHTML = " Removed !"
        message.style.color = 'saddlebrown'
        document.getElementById('coupon_div').appendChild(message)
        $('#coupon_apl_btn').show()
        $('#coupon_rmv_btn').hide()
        $('#coupon_field').val('')
        $('#cb').empty()
        $('#f_amt').text($('#ttl_amt').text())
      }
      else{
        new_data = arr[4].split("^")
        new_total = new_data[1]
        cashback = new_data[2]
        $('#f_amt').text(new_total)
        $('#cb_price').text(cashback)
      }
    }
  })
}