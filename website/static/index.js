// Javascript function to delete a note, given the note id
function deleteNote(noteId) {
  // fecth is a function that sends a request to an endpoint
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  // Reloads the window to the home page after it gets a response from the request
  }).then((_res) => {
    window.location.href = "/";
  });
}