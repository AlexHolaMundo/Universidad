$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z\s]*$/.test(value)
    },
    'Solo se permiten letras en este campo'
  )
  $('#formCarreraWATT').validate({
    rules: {
      idCarreraWATT: {
        required: true,
      },
      nombreCarreraWATT: {
        required: true,
        lettersonly: true,
        minlength: 10,
        maxlength: 10,
      },
      logoCarreraWATT: {
        required: true,
        extension: 'jpg|png|jpeg',
      },
      directorCarreraWATT: {
        required: true,
        lettersonly: true,
        minlength: 3,
        maxlength: 50,
      },
      fechaCreacionCarreraWATT: {
        required: true,
        date: true,
      },
      descripcionCarreraWATT: {
        required: true,
        lettersonly: true,
      },
    },
    messages: {
      idCarreraWATT: {
        required: 'El id de la carrera es obligatorio',
      },
      nombreCarreraWATT: {
        required: 'El nombre de la carrera es obligatorio',
        lettersonly: 'Solo se permiten letras en este campo',
        minlength: 'El nombre de la carrera debe tener al menos 10 caracteres',
        maxlength:
          'El nombre de la carrera debe tener como máximo 10 caracteres',
      },
      logoCarreraWATT: {
        required: 'El logo de la carrera es obligatorio',
        extension: 'Solo se permiten archivos jpg, png y jpeg',
      },
      directorCarreraWATT: {
        required: 'El director de la carrera es obligatorio',
        lettersonly: 'Solo se permiten letras en este campo',
        minlength: 'El director de la carrera debe tener al menos 3 caracteres',
        maxlength:
          'El director de la carrera debe tener como máximo 50 caracteres',
      },
      fechaCreacionCarreraWATT: {
        required: 'La fecha de creación de la carrera es obligatoria',
        date: 'El formato de la fecha no es válido',
      },
      descripcionCarreraWATT: {
        required: 'La descripción de la carrera es obligatoria',
        lettersonly: 'Solo se permiten letras en este campo',
      },
    },
  })
})

$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z\s]*$/.test(value)
    },
    'Solo se permiten letras en este campo'
  )
  $('#formCursosWATT').validate({
    rules: {
      idCursoWATT: {
        required: true,
      },
      nivelCursoWATT: {
        required: true,
        minlength: 10,
        maxlength: 10,
      },
      descripcionCursoWATT: {
        required: true,
        lettersonly: true,
        minlength: 3,
        maxlength: 50,
      },
      aulaCursoWATT: {
        required: true,
        lettersonly: true,
      },
      horarioCursoWATT: {
        required: true,
        extension: 'jpg|png|jpeg',
      },
      nombreCarreraWATT: {
        required: true,
        date: true,
      },
    },
    messages: {
      idCursoWATT: {
        required: 'El id de la carrera es obligatorio',
      },
      nivelCursoWATT: {
        required: 'El nivel del curso es obligatorio',
        minlength: 'El nivel del curso debe tener al menos 10 caracteres',
        maxlength: 'El nivel del curso debe tener como máximo 10 caracteres',
      },
      descripcionCursoWATT: {
        required: 'La descripción del curso es obligatoria',
        lettersonly: 'Solo se permiten letras en este campo',
        minlength: 'La descripción del curso debe tener al menos 3 caracteres',
        maxlength:
          'La descripción del curso debe tener como máximo 50 caracteres',
      },
      aulaCursoWATT: {
        required: 'El aula del curso es obligatoria',
        lettersonly: 'Solo se permiten letras en este campo',
      },
      horarioCursoWATT: {
        required: 'El horario del curso es obligatorio',
        extension: 'Solo se permiten archivos jpg, png y jpeg',
      },
      nombreCarreraWATT: {
        required: 'El nombre de la carrera es obligatorio',
      },
    },
  })
})

$(document).ready(function () {
  $.validator.addMethod(
    'lettersonly',
    function (value, element) {
      return this.optional(element) || /^[a-zA-Z\s]*$/.test(value)
    },
    'Solo se permiten letras en este campo'
  )
  $('#formAsignaturasWATT').validate({
    rules: {
      idAsignaturaWATT: {
        required: true,
      },
      nombreAsignaturaWATT: {
        lettersonly: true,
        required: true,
        minlength: 10,
        maxlength: 10,
      },
      creditosAsignaturaWATT: {
        required: true,
        number: true,
        minlength: 3,
        maxlength: 50,
      },
      fechaInicioAsignaturaWATT: {
        date: true,
        required: true,
      },
      fechaFinalizacionAsignaturaWATT: {
        date: true,
        required: true,
      },
      profesorAsignaturaWATT: {
        required: true,
        lettersonly: true,
      },
      silaboAsignaturaWATT: {
        required: true,
        extension: 'pdf',
      },
      departamentoAsignaturaWATT: {
        required: true,
        lettersonly: true,
      },
      nivelCursoWATT: {
        required: true,
        lettersonly: true,
      },
      descripcionCarreraWATT: {
        required: true,
        lettersonly: true,
      },
    },
    messages: {
      idAsignaturaWATT: {
        required: 'El id de la carrera es obligatorio',
      },
      nombreAsignaturaWATT: {
        required: 'El nombre de la asignatura es obligatorio',
        lettersonly: 'Solo se permiten letras en este campo',
        minlength:
          'El nombre de la asignatura debe tener al menos 10 caracteres',
        maxlength:
          'El nombre de la asignatura debe tener como máximo 10 caracteres',
      },
      creditosAsignaturaWATT: {
        required: 'Los créditos de la asignatura son obligatorios',
        number: 'Solo se permiten números en este campo',
        minlength:
          'Los créditos de la asignatura deben tener al menos 3 caracteres',
        maxlength:
          'Los créditos de la asignatura deben tener como máximo 50 caracteres',
      },
      fechaInicioAsignaturaWATT: {
        required: 'La fecha de inicio de la asignatura es obligatoria',
        date: 'El formato de la fecha no es válido',
      },
      fechaFinalizacionAsignaturaWATT: {
        required: 'La fecha de finalización de la asignatura es obligatoria',
        date: 'El formato de la fecha no es válido',
      },
      profesorAsignaturaWATT: {
        required: 'El profesor de la asignatura es obligatorio',
        lettersonly: 'Solo se permiten letras en este campo',
      },
      silaboAsignaturaWATT: {
        required: 'El silabo de la asignatura es obligatorio',
        extension: 'Solo se permiten archivos pdf',
      },
      departamentoAsignaturaWATT: {
        required: 'El departamento de la asignatura es obligatorio',
        lettersonly: 'Solo se permiten letras en este campo',
      },
      nivelCursoWATT: {
        required: 'El nivel del curso es obligatorio',
        lettersonly: 'Solo se permiten letras en este campo',
      },
      descripcionAsignaturaWATT: {
        required: 'La descripción de la carrera es obligatoria',
        lettersonly: 'Solo se permiten letras en este campo',
      },
    },
  })
})
