$(window).scroll(function () {
if ($(window).scrollTop() >= 250) {
$('.navbar').css('background','#0e1111');
} else {
$('.navbar').css('background','transparent');
}
});