
function translating(){
    var myDataVar = {};
    // myDataVar.text_area = $('#text_area').val();
    myDataVar['text_area'] = $('#text_area').val();
    myDataVar['option'] = $('#option').val();

    $.ajax({
        type: "POST",
        url: "translating",   
        data: myDataVar,
        success: function(resultData){
           console.log(resultData)
           $('#result_area').val(resultData.translated_text_is);

        },
        error: function() { }
    });
}