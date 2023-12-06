(function(){
    const btnaction = document.querySelectorAll(".btnaction");
    btnaction.forEach(btn =>{
        btn.addEventListener('click', (e) =>{
              const confirmar= confirm('Seguro que quieres selecionar el usuario');
              if(!confirmar){
                e.preventDefault();
              }
        });
    });
})();

