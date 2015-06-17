$(function() {
    var pages, path;
    $(".button-collapse").sideNav({
      edge: 'left'
    });
    path = window.location.pathname;
    pages = ['/about-me/', '/blog/', '/find-me/', '/resume/', '/playground/'];
    if (path === '/') {
        url = $(location).attr('href')
        url += 'about-me/'
        $(location).attr('href', url);
    }
    if (pages.indexOf(path) > -1) {
      $("#navigation").children().removeClass('active');
      $("#navigation").find("a[href=\"" + path + "\"]").parent().addClass('active');
    }
});


// jQuery(function() {


//   var pages, path, typeBox;
//   $(".button-collapse").sideNav({
//     edge: 'left'
//   });
//   path = window.location.pathname;
//   pages = ['/about-me/', '/blog/', '/find-me/', '/resume/', '/playground/'];
//   if (path === '/') {
//     typeBox = new typeBox();
//     typeBox.initHeadline();
//   }
//   if (indexOf.call(pages, path) >= 0) {
//     $("#navigation").children().removeClass('active');
//     $("#navigation").find("a[href=\"" + path + "\"]").parent().addClass('active');
//   }
// });

// jQuery ->

//   $(".button-collapse").sideNav({
//   edge: 'left'
//   })

//   path = window.location.pathname
//   pages = ['/about-me/', '/blog/', '/find-me/', '/resume/', '/playground/']

//   if path is '/'
//     typeBox = new typeBox()
//     typeBox.initHeadline()

//   if path in pages
//     $("#navigation").children().removeClass('active')
//     $("#navigation").find("a[href=\"#{path}\"]").parent().addClass('active')
    

//   return