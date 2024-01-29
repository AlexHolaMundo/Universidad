//Paginacion y filtrado de la tabla de provincias
$(document).ready(function () {
  let table = $('#tableCarreras').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Detalles de las Provincias',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [5],
        className: 'acciones-column',
      },
    ],
  })
})

//Paginacion y filtrado de la tabla de provincias
$(document).ready(function () {
  let table = $('#tableAsignaturas').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Detalles de las Provincias',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [5],
        className: 'acciones-column',
      },
    ],
  })
})

$(document).ready(function () {
  let table = $('#tableCursos').DataTable({
    searching: true,
    fixedHeader: true,
    paging: true,
    info: true,
    pageLength: 5,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json',
    },
    dom: 'Bfrtip',
    buttons: [
      {
        extend: 'pdfHtml5',
        text: 'Exportar a PDF <i class="fas fa-file-pdf"></i>',
        title: 'Detalles de las Provincias',
        className: 'btn btn-danger',
        exportOptions: {
          columns: ':visible:not(.acciones-column)',
        },
        init: function (api, node, config) {
          $(node).removeClass('dt-button')
          $(node).prepend('<i class="fas fa-file-pdf"></i>')
        },
      },
      {
        extend: 'print',
        text: 'Imprimir <i class="fas fa-print"></i>',
        className: 'btn btn-warning',
      },
      {
        extend: 'csv',
        text: 'Exportar a CSV <i class="fas fa-file-csv"></i>',
        className: 'btn btn-success',
      },
    ],
    columnDefs: [
      {
        targets: [5],
        className: 'acciones-column',
      },
    ],
  })
})
