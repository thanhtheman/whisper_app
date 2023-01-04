document.addEventListener('DOMContentLoaded', () => {});

  // document.addEventListener('DOMContentLoaded', function () {
  //   hljs.highlightAll();
  // });
  
  
  let alertWrapper = document.getElementById('alert')
  let alertClose = document.getElementById('alert__close')
  
  if (alertWrapper) {
    alertClose.addEventListener('click', () => {
      alertWrapper.style.display = 'none';
      alertClose.style.display = 'none';
    })
  }