$('.datepicker').datepicker({
    weekStart:1,
    color: 'red'
});

$('.bookticket').on('click',function(){
    var link_path=$(this).attr('href') + $(this).siblings('.datepicker').val()+'/';
    $(this).attr('href',link_path);
    window.location.href=link_path;
})

$('#seat_planning').on('click','.avail',function(){
    if($('#id_seatnumber').attr('data-value')==''){
        $('#id_seatnumber').attr('data-value',$(this).text()+', ');
        $('#id_seatnumber').val($(this).text()+', ')
    }else{
        var i = $('#id_seatnumber').attr('data-value')+' '+$(this).text()+',';
        $('#id_seatnumber').attr('data-value',i)
        $('#id_seatnumber').val(i)
    }
    if($('#id_totalprice').val()==0){
        $('#id_totalprice').val($('#tp').val());
    }else{
        var p=parseInt($('#tp').val())+parseInt($('#id_totalprice').val());
        $('#id_totalprice').val(p);
    }
    $(this).removeClass('avail').addClass('reserve');
})

$('#seat_planning').on('click','.reserve',function(){
    var i=$('#id_seatnumber').attr('data-value')+' ';
    var r=$(this).text()+', ';
    var seatupdate=i.replace(r,'')
    $('#id_seatnumber').attr('data-value',seatupdate);
    $('#id_seatnumber').val(seatupdate);
    var p=parseInt($('#id_totalprice').val()) - parseInt($('#tp').val());
    $('#id_totalprice').val(p);
    $('#id_totalprice').attr('value',p)
    $(this).removeClass('reserve').addClass('avail');
})

$( "#seat_planning td" ).each(function( index ) {
    var r='';
    var n='';
    r=$('.reser').text();
    //console.log(r)
    // n= r.indexOf($( this ).text());
    // if(n>=0){
    //     //console.log( index + ": " + $( this ).text() );
    //     $(this).children('a').removeClass('avail');
    //     $(this).children('a').addClass('booked');
    // }
    var pattern = new RegExp("(^|\\W)" + $(this).text() + "($|\\W)");
    if(r.match(pattern)){
        $(this).children('a').removeClass('avail');
        $(this).children('a').addClass('booked');
    }
});

if($('.updateseat').children('input').attr('data-value')!='undefined'){
    $( "#seat_planning td" ).each(function( index ) {
        var r='';
        var n='';
        r=$('.updateseat').children('input').attr('data-value');
        $('.updateseat').children('input').val(r+' ');
       // n= r.indexOf($(this).text());
        // if(n>=0){
        //     console.log( index + ": " + $( this ).text() );
        //     $(this).children('a').removeClass('booked');
        //     $(this).children('a').addClass('reserve');
        // }
        var pattern = new RegExp("(^|\\W)" + $(this).text() + "($|\\W)");
        if(r.match(pattern)){
            $(this).children('a').removeClass('booked');
            $(this).children('a').addClass('reserve');
        }
    })
}

$('.preview').on('click',function(){
    $('.previewimage').attr('src',$(this).attr('rel'));

})

$('.delveh').on('click',function(){
    $('#deleteModal .btn-danger').attr('href',$(this).attr('rel'));
})