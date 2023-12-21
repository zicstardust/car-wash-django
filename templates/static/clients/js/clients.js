function add_car(){

    container = document.getElementById("form-car")

    html = "<br><div class='row'> \
    <div class='col-md'> <input type='text' placeholder='Car' class='form-control' name=''></div> \
    <div class='col-md'><input type='text' placeholder='Plate' class='form-control'> </div>\
    <div class='col-md'><input type='number' placeholder='Year' class='form-control'> </div>\
    </div>";

    container.innerHTML += html

};