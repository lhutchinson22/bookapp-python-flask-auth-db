function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId })
  }).then(_res => {
    window.location.href = "/";
  });
}

function searchBooks() {
  const query = document.getElementById("book-search").value;
  fetch(`/search-books?query=${query}`)
    .then(response => response.json())
    .then(books => {
      const resultsDiv = document.getElementById("book-results");
      resultsDiv.innerHTML = "";
      books.forEach(book => {
        const bookItem = document.createElement("div");
        bookItem.classList.add("list-group-item");
        bookItem.innerHTML = `
          ${book.volumeInfo.title}
          <button class="btn btn-sm btn-primary" onclick="selectBook('${book.volumeInfo.title}')">Select</button>
        `;
        resultsDiv.appendChild(bookItem);
      });
    });
}

function selectBook(title) {
  document.getElementById("selected-book-title").value = title;
  document.getElementById("book-results").innerHTML = "";
  document.getElementById("book-search").value = title;
}
