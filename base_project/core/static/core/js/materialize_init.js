$(() => {
    $('.tabs').tabs();
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
    $('.carousel').carousel({
		fullWidth: true,
		indicators: true,
		duration: 500,
	});
    $('.dropdown-trigger:not(.select-dropdown)').dropdown({
        coverTrigger: false,
        constrainWidth: false,
        alignment: 'right',
        hover: true,
    });
	setInterval(function(){
        $(".carousel").carousel("next");
    }, 7000);
});