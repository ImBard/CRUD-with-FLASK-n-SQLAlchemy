function openModal(name, age, email) {
  const exampleModal = document.getElementById('exampleModal')
  const inputName = document.getElementById('name')
  const inputAge = document.getElementById('age')
  const inputEmail = document.getElementById('email')
  const form = document.getElementById("formUpdate")
    // Button that triggered the modal
    const button = document.getElementById("buttonModal")
    // Extract info from data-bs-* attributes
    const recipient = button.getAttribute('data-bs-whatever')
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    const modalTitle = exampleModal.querySelector('.modal-title')
    const modalBodyInput = exampleModal.querySelector('.modal-body input')

    modalTitle.textContent = `Atualizar dados de ${recipient}`
    inputAge.value = age
    inputEmail.value = email
    inputName.value = name
    form.action = `/update/${email}`
}