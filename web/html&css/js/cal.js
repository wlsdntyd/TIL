var btn = document.getElementById('btn-add');
btn.onclick = function () {
    var x = document.getElementById('txt-x').value;
    var y = document.getElementById('txt-y').value;
    var result = document.getElementById('txt-sum');

    if (document.getElementsByName('add')[0].checked == true) {
        result.value = parseInt(x) + parseInt(y);
    }
    else if (document.getElementsByName('sub')[0].checked == true) {
        result.value = parseInt(x) - parseInt(y);
    }
    else if (document.getElementsByName('mul')[0].checked == true) {
        result.value = parseInt(x) * parseInt(y);
    }
    else if (document.getElementsByName('div')[0].checked == true) {
        result.value = parseInt(x) / parseInt(y);
    }
}