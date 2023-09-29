$(document).ready(function () {
/* 
    Show Welcome Modal
  */

  const pathname = window.location.pathname; // get the path of the URL
  const hasUserProfile = $('main').data('userprofile'); // get the user profile
  const isAuth = $('main').data('isauth'); // get if is auth
  const myModal = new bootstrap.Modal(document.getElementById('modalWelcome'));
  if (pathname === '/' && hasUserProfile === '' && isAuth !== 'False') {
    myModal.show();
  }   
  
  /* 
    Add plugins Jquery Select 2 to the select of categories
  */

    $('#small-bootstrap-class-multiple-field').select2({
      theme: "bootstrap-5",
      width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
      placeholder: $(this).data('placeholder'),
      closeOnSelect: false,
      dropdownParent: $('#small-bootstrap-class-multiple-field').parent(),
    });

  /* 
    show notifications
  */

    var flashMessages = document.querySelectorAll('.messages');
    flashMessages.forEach(function (message) {
      setTimeout(function () {
        message.style.display = 'none';
      }, 5000); // 5000 milliseconds (5 seconds)
    });

    /* 
      Show/Hidden section comment in the list of post when user click comment button
      Hide: add class of boostrap 'd-none'
      Show: remove class of boostrap 'd-none'
    */
    $("#post-lists").on('click', '#open-comments', function (e) {
      e.preventDefault();
      // get id of the post
      const id = $(this).data('post');
      const element = $('#comments_' + id);
      if (element.hasClass('d-none')) {
        $('#comments_' + id).removeClass('d-none');
      } else {
        $('#comments_' + id).addClass('d-none');
      }

    });

    /* 
      Catch event for delete in Category List or Post to show confirm windows 
      in case confirm submit the form if not just stop the event
    */
    $("#category_list, #post_actions").on('click', '.delete-button', function (e) {
      e.preventDefault(); // stop the form
      const form = $(this);
      $.confirm({
        title: 'Are you sure ?',
        content: $(this).data('title'),
        buttons: {
          confirm: function () {            
            form.submit();
          },
          cancel: function () {
            e.preventDefault();              
          },
        }
      });
    });
  });