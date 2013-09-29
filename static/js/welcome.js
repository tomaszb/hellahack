	R.ready(function() { // just in case the API isn't ready yet
	//  if (R.authenticated() == true){
	// 	window.location.href = "/player/";
		$("#signin").click(function() {
			if (R.authenticated() == false){
				R.authenticate(function () {

					document.location.href = "/player/";
				});
			} else {
				document.location.href = "/player/";
			}
		});

	});