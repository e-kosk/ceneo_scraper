$(document).ready( function () {
    $('#table').DataTable();

    $('#collapse-button').on('click', function () {
        $('#collapse-button-arrow').toggleClass('fa-arrow-down').toggleClass('fa-arrow-up')
    })
} );