  (function() {

  window.Main = {
    // ----------
    init: function() {
  $(document).ready(function() {
    Main.init();
  });
  
})(); /*globals R, Main, Modernizr, rdioUtils */

(function() {

  window.Main = {
    // ----------
    init: function() {
    if (R.authenticated == false){
    	R.authenticate()
    }

    //window.location = 


  };
  
  // ----------
  $(document).ready(function() {
    Main.init();
  });
  
})();  
