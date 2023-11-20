  function displayModal() {
        const modal = document.getElementById('age-verification-modal');
        modal.style.display = 'block';
  }

  const hasSeenModal = sessionStorage.getItem('hasSeenModal');
  if (hasSeenModal !== 'true') {
      displayModal();
      sessionStorage.setItem('hasSeenModal', 'true');
  }

  document.getElementById('verify-age').addEventListener('click', function() {
    const birthDate = document.getElementById('birth_date').value;
    if (birthDate !== undefined && birthDate !== '') {
        const dateObject = new Date(birthDate);
        const dayOfWeek = dateObject.getDay();
        const dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        alert(dayNames[dayOfWeek]);
    }
    else {
        alert('Дата не выбрана');
        return;
    }

    const age = calculateAge(birthDate);

    if (age >= 18) {
      document.getElementById('age-verification-modal').style.display = 'none';
    } else {
      alert('Вы несовершеннолетний. Требуется разрешение родителей.');
    }
  });

  function calculateAge(birthDate) {
    const today = new Date();
    const dob = new Date(birthDate);
    let age = today.getFullYear() - dob.getFullYear();
    const monthDiff = today.getMonth() - dob.getMonth();

    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dob.getDate())) {
        age--;
    }
    return age;
  }