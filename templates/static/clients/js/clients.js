function add_car(){

    container = document.getElementById("form-car")

    html = "<br><div class='row'> \
    <div class='col-md'> <input type='text' placeholder='Car' class='form-control' name='car'></div> \
    <div class='col-md'><input type='text' placeholder='Plate' class='form-control' name='plate'> </div>\
    <div class='col-md'><input type='number' placeholder='Year' class='form-control' name='year'> </div>\
    </div>";

    container.innerHTML += html

};