function enviar_ajax() {
    usuario = 42;

    var origin = $("#origin").val();
    var destiny = $("#destiny").val();
    var time = $("#time").val();
    var plan = $("#plans").val();

    data = {
        "origin": origin,
        "destiny": destiny,
        "time": time,
        "plan": plan
    }
    const post_usuario = JSON.stringify(usuario);

    $.ajax({
        url: '/calc_plan',
        type: 'POST',
        data: JSON.stringify(data),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function (result, status, request) {
            if (result.length > 1) {
                 var priceWith = result[0].toLocaleString("pt-BR", { style: "currency" , currency:"BRL"});
                var priceWithout = result[1].toLocaleString("pt-BR", { style: "currency" , currency:"BRL"});
                $("#pricewith").text(priceWith)
                $("#pricewithout").text(priceWithout)
                    console.log(result);
            } else {
                 var priceWith = '-'
                 var priceWithout = '-'
                  $("#pricewith").text(priceWith)
                $("#pricewithout").text(priceWithout)
                    console.log(result);
            }
        },
        error: function (event, jqxhr, settings, thrownError) {

            console.log('event: ' + JSON.stringify(event));
//            console.log('jqxhr: ' + jqxhr);
//            console.log('settings: ' + settings);
//            console.log('thrownError: ' + thrownError);
//            alert('Error');
        }
    });
}