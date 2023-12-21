function add_car(){

    document.getElementById('form-car').innerHTML +=
    "<br>\
    <div class='row'> \
    <div class='col-md'> <input type='text' placeholder='car' class='form-control' name='car'></div> \
    <div class='col-md'><input type='text' placeholder='plate' class='form-control' name='plate'> </div> \
    <div class='col-md'><input type='number' placeholder='year' class='form-control' name='year'> </div>\
    </div>"

}