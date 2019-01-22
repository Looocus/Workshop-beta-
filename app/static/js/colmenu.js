$(document).ready(function() {
  function showpanel() {
		$('.container').removeClass('startup');
    $('.ball').addClass('active').delay(2000).queue(function(next) {
			$(this).removeClass('active');
			next();
		});
 	}
	$('.ball').click(function() {
		$(this).toggleClass('active');
	});
 setTimeout(showpanel, 1800);
});

function changered(){
	document.getElementById("ballid").style.background="#ff7f7f";
	var elements = document.getElementsByClassName("btnall");
	for (var ele in elements) {
		elements[ele].style.backgroundColor="#ff7f7f";
	};
}