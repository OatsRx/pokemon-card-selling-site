/* Payment logic from stripe documentation */

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

/* Styles from stripe documentation */
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

/* Form submit logic from stripe documentation and modified */
var form = document.getElementById('payment-form');


form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#confirm-payment').attr('disabled', true);

    var saveInfo = Boolean($('#id-save-details').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_detaill: {
                    name: (form.full_name.value),
                    phone: (form.phone_number.value),
                    email: (form.email.value),
                    address: {
                        line1: (form.street_address1.value),
                        line2: (form.street_address2.value),
                        city: (form.town_or_city.value),
                        country: (form.country.value),
                        county: (form.county.value),
                    }
                }
            }
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false });
                $('#confirm-payment').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // fail/400 request
        location.reload();
    })
});