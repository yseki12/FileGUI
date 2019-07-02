$(document).ready(function () {
    $('#customSwitch1').change(function () {
        if (!this.checked) 
            $('#indexTable tr td:contains(No)').parent().fadeIn('fast');
        else 
            $('#indexTable tr td:contains(No)').parent().hide();

        $("#indexTable tr:visible").each(function (index) {
            $(this).css("background-color", !!(index & 1)? "rgba(0,0,0,0)" : "rgba(0,0,0,0.05)");
    });
    });
    $('#customSwitch1').change();

});
