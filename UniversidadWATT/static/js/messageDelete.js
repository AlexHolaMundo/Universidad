function eliminarCarrera(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar la carrera seleccionada?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}

function eliminarCurso(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar el curso seleccionado??',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}

function eliminarAsignatura(url) {
  ' '
  {
    iziToast.question({
      timeout: 15000,
      close: true,
      overlay: true,
      displayMode: 'once',
      id: 'question',
      zindex: 999,
      title: 'CONFIRMACIÓN',
      message: '¿Está seguro de eliminar la asignatura seleccionada?',
      position: 'center',
      buttons: [
        [
          '<button><b>SI</b></button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
            window.location.href = url
          },
          true,
        ],
        [
          '<button>NO</button>',
          function (instance, toast) {
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button')
          },
        ],
      ],
    })
  }
}
