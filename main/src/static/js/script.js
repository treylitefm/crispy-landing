$(document).ready(function(){
    var csrftoken = $.cookie('csrftoken')

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('.new-page').on('click', function(e) {
        $('.hidden').removeClass('hidden')
    });

    $('.launch').on('click', function() {
        var page_id = $(this).attr('data-page-id');

        $.ajax({
            type: 'POST',
            url: '/tests/create/'+page_id,
            data: {
                'browser': $('.browser-control').val()
            },
            success: function() {
                $('.status-'+page_id).addClass('orange')
            },
            dataType: 'json'
        })
        return false;
    });

    $('.activate').on('click', function() {
        var page_id = $(this).attr('data-page-id')
        var launch = $('.launch-'+page_id)
        launch.prop('disabled', !launch.prop('disabled'))
        
        $.ajax({
            type: 'POST',
            url: '/pages/edit/'+String(page_id),
            data: {'enabled': $('.activate-'+page_id).prop('checked')},
            dataType: 'json'
        })
    });

    /*
    $('.page-anchor').on('click', function() {
        var page_id = $(this).attr('data-page-id');
        $.ajax({
            type: 'GET',
            url: '/tests/get/all/'+page_id,
            success: function(res) {
                var canon = $('.canon-thumb-wrapper').clone()
                $('.thumbnail-container').html('')
                    console.log('poormamro')
                for (var i = 0; i < res['tests'].length; i++) { 
                    var newTag = canon
                    console.log('yommomomo', canon, newTag)
                    newTag.attr('href', '/static/img/'+res['tests'][i][1])
                    newTag.children().css('background-image', 'url(/static/img/'+res['tests'][i][1]+')')
                    newTag.children().css('background-size', 'cover')
                    newTag.removeClass('hidden')
                    newTag.children().removeClass('hidden')
                    newTag.removeClass('canon-thumb-wrapper')
                    document.newTag = newTag
                    console.log('yommomomo', canon, newTag)
                    $('.thumbnail-container').append(newTag)
                }
            }
        })
    });*/

    $('[data-toggle="tooltip"]').tooltip()

    $(document).on('click', '[data-toggle="lightbox"]', function(event) {
            event.preventDefault();
                $(this).ekkoLightbox();
    });

    $(document).keypress(function(e) { 
        if (e.keycode == '13') {
            return false
        }
    
    });
})
