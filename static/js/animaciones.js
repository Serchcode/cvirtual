<script>
$(document).ready(function animacion_top(){

    $('#page-top').click(function(){
        $('body, html').animate({
            scrollTop: '0px'
        }, 1000);
    });

    $(window).scroll(function(){
        if( $(this).scrollTop() > 0 ){
            $('#page-top').slideDown(1000);
        } else {
            $('.page-top').slideUp(1000);
        }
    });

});
</script>