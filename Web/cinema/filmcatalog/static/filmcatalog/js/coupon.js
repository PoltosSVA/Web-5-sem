document.getElementById("applyCoupon").addEventListener("click", function() {
  const couponCode = document.getElementById("couponCode").value;
  fetch(`http://127.0.0.1:8000/cart/validate_coupon/?coupon_code=${couponCode}`)
    .then(response => response.json())
    .then(data => {
      if (data.discount !== undefined) {

        const discount = data.discount;
        updateCartTotal(discount);

        document.getElementById("couponCode").disabled = true
        document.getElementById("applyCoupon").disabled = true
      } else {
        }
      });
});

function updateCartTotal(discount) {
    const currentTotal = parseFloat(document.getElementById("totalPrice").textContent);
    const newTotal = currentTotal - currentTotal * (discount / 100 );
    document.getElementById("totalPrice").textContent = String(newTotal.toFixed(2));
}