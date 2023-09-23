$(document).ready(function () {

    $('#small-bootstrap-class-multiple-field').select2({
      theme: "bootstrap-5",
      width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
      placeholder: $(this).data('placeholder'),
      closeOnSelect: false,
      dropdownParent: $('#small-bootstrap-class-multiple-field').parent(),
    });


    var flashMessages = document.querySelectorAll('.alert-success');
    flashMessages.forEach(function (message) {
      setTimeout(function () {
        message.style.display = 'none';
      }, 5000); // 5000 milliseconds (5 seconds)
    });

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


    $("#category_list, #post_actions").on('click', '.delete-button', function (e) {
      e.preventDefault(); // stop the form
      const form = $(this);
      console.log(form)
      $.confirm({
        title: 'Are you sure ?',
        content: $(this).data('title'),
        buttons: {
          confirm: function () {            
            form.submit()
          },
          cancel: function () {
            e.preventDefault();              
          },
        }
      });
    });

  });