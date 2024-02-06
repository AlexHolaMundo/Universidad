//Charts carreras
document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('chartCarrera')

  const nombresSet = new Set()
  const nombres = {}

  ;`{% for carrera in carreras %}`
  nombresSet.add('{{ carrera.nombreCarreraWATT }}')
  if (!nombres['{{ carrera.nombreCarreraWATT }}']) {
    nombres['{{ carrera.nombreCarreraWATT }}'] = 1
  } else {
    nombres['{{ carrera.nombreCarreraWATT }}'] += 1
  }
  ;`{% endfor %}`
  const nombresArray = Array.from(nombresSet)
  const posiciones = nombresArray.map((tipo, index) => ({
    x: index,
    y: nombres[tipo] || 0,
  }))

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: nombresArray,
      datasets: [
        {
          label: 'Cantidad de carreras',
          data: posiciones.map((posicion) => posicion.y),
          backgroundColor: 'rgba(75, 192, 192, 0.5)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: 'category',
          position: 'bottom',
        },
        y: {
          beginAtZero: true,
          max: 10,
          stepSize: 1,
        },
      },
    },
  })
  window.toggleChart = function () {
    const chartContainer = document.getElementById('chartContainer')

    if (chartContainer.style.display === 'none') {
      chartContainer.style.display = 'block'
    } else {
      chartContainer.style.display = 'none'
    }
  }
})
//Charts cursos
document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('chartCurso')

  const nivelSet = new Set()
  const niveles = {}

  ;`{% for carrera in carreras %}`
  nivelSet.add('{{ carrera.nivelCursoWATT }}')
  if (!niveles['{{ carrera.nivelCursoWATT }}']) {
    niveles['{{ carrera.nivelCursoWATT }}'] = 1
  } else {
    niveles['{{ carrera.nivelCursoWATT }}'] += 1
  }
  ;`{% endfor %}`

  const nivelesArray = Array.from(nivelSet)
  const posiciones = nivelesArray.map((tipo, index) => ({
    x: index,
    y: niveles[tipo] || 0,
  }))

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: nivelesArray,
      datasets: [
        {
          label: 'Cantidad de niveles',
          data: posiciones.map((posicion) => posicion.y),
          backgroundColor: 'rgba(75, 192, 192, 0.5)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: 'category',
          position: 'bottom',
        },
        y: {
          beginAtZero: true,
          max: 10,
          stepSize: 1,
        },
      },
    },
  })

  window.toggleChart = function () {
    const chartContainer = document.getElementById('chartContainer')

    if (chartContainer.style.display === 'none') {
      chartContainer.style.display = 'block'
    } else {
      chartContainer.style.display = 'none'
    }
  }
})

//Charts asignaturas
document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('chartAsignatura')

  const asignaturaSet = new Set()
  const asignaturas = {}

  ;`{% for asignatura in asignaturas %}`
  asignaturaSet.add('{{ asignatura.nombreAsignaturaWATT }}')
  if (!asignaturas['{{ asignatura.nombreAsignaturaWATT }}']) {
    asignaturas['{{ asignatura.nombreAsignaturaWATT }}'] = 1
  } else {
    asignaturas['{{ asignatura.nombreAsignaturaWATT }}'] += 1
  }
  ;`{% endfor %}`

  const asignaturasArray = Array.from(asignaturaSet)
  const posiciones = asignaturasArray.map((tipo, index) => ({
    x: index,
    y: asignaturas[tipo] || 0,
  }))

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: asignaturasArray,
      datasets: [
        {
          label: 'Cantidad de asignaturas',
          data: posiciones.map((posicion) => posicion.y),
          backgroundColor: 'rgba(75, 192, 192, 0.5)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: 'category',
          position: 'bottom',
        },
        y: {
          beginAtZero: true,
          max: 10,
          stepSize: 1,
        },
      },
    },
  })

  window.toggleChart = function () {
    const chartContainer = document.getElementById('chartContainer')

    if (chartContainer.style.display === 'none') {
      chartContainer.style.display = 'block'
    } else {
      chartContainer.style.display = 'none'
    }
  }
})
