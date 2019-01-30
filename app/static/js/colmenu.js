$(document).ready(function() {
	function showpanel() {
		$('.container').removeClass('startup');
		$('.ball').addClass('active').delay(2000).queue(function(next) {
			$(this).removeClass('active');
			next();
		});
 	};
	$('.ball').click(function() {
		$(this).toggleClass('active');
	});
 setTimeout(showpanel, 1800);
});

function changered(){
	document.getElementById("ballid").style.background="#ff7f7f";
	var elements = document.getElementsByClassName("btnall");
	for (var ele in elements) {
		elements[ele].style.background="#ff7f7f";
	};
};

function changeblue(){
	document.getElementById("ballid").style.background="#8484ff";
	var elements = document.getElementsByClassName("btnall");
	for (var ele in elements) {
		elements[ele].style.background="#8484ff";
	};
};

function changegreen(){
	document.getElementById("ballid").style.background="#89ff89";
	var elements = document.getElementsByClassName("btnall");
	for (var ele in elements) {
		elements[ele].style.background="#89ff89";
	};
};

function changepink(){
	document.getElementById("ballid").style.background="#ff7fc7";
	var elements = document.getElementsByClassName("btnall");
	for (var ele in elements) {
		elements[ele].style.background="#ff7fc7";
	};
};

function changeorange(){
	document.getElementById("ballid").style.background="#ffc78a";
	var elements = document.getElementsByClassName("btnall");
	for (var ele in elements) {
		elements[ele].style.background="#ffc78a";
	};
};

