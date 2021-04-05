// variable that keeps all the filter information

var send_data = {}

$(document).ready(function () {
    // reset all parameters on page load

    resetFilters();
    // bring all the data without any filters

    getAPIData();
    // get all countries from database via

    // AJAX call into country select options

    get_research_type();
    // get all varities from database via

    // AJAX call into variert select options

    $('#countries').on('change', function () {
        // since province and region is dependent
        // on country select, emty all the options from select input
        $("#province").val("all");
        $("#region").val("all");
        send_data['province'] = '';
        send_data['region'] = '';

        // update the selected country
        if(this.value == "all")
            send_data['country'] = "";
        else
            send_data['country'] = this.value;

        //get province of selected country
        getProvince(this.value);
        // get api data of updated filters
        getAPIData();
    });
});