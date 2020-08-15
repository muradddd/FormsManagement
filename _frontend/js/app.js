$('.dropdown-toggle').dropdown()

$('#myDropdown').on('show.bs.dropdown', function () {
    // do something…
});

var index = 0;
const addField = () => {
  var fieldSection = ` <section class="second-section">
                          <div class="additional-content"
                          <div div class="field-div col-12">
                            <div class="row pt-1 pl-3">
                              <div class="col-8">
                                <div class="form-group">
                                  <p>Question</p>
                                  <input type="text" name="fieldIndex-${index}-question" maxlength="1001" required="" id="id_question">
                                </div>
                              </div>
                              <div class="col-4">
                                <div class="form-group">
                                  <p>Answer type</p>
                                  <select name="fieldIndex-${index}-answer_type" required="" id="id_answer_type">
                                    <option value="text">Short answer</option>
                                    <option value="textarea">Paragraph</option>
                                    <option value="radio choice">Multiple choice</option>
                                    <option value="checkbox">Checkboxes</option>
                                    <option value="select">Dropdown</option>
                                    <option value="date">Date</option>
                                  </select>
                                </div>
                              </div>
                              <div class="col-12">
                                <div class="row">
                                  <div class="offset-6 col-2">
                                    <div class="icons-opt">
                                      <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-trash" fill="currentColor"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path
                                          d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z">
                                        </path>
                                        <path fill-rule="evenodd"
                                          d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z">
                                        </path>
                                      </svg>
                                    </div>
                                  </div>
                                  <div class="col-4">
                                    <div class="form-group">
                                      <span>Required<b>*</b></span>
                                      <form action="#">
                                        <div class="switch">
                                        <input id="switch-1" type="checkbox" name="fieldIndex-${index}-is_required" id="id_is_required" class="switch-input" />
                                        <label for="switch-1" class="switch-label">Switch</label>
                                    </div>
                                    </form>
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <a href="./form-detail.html"><button type="button" class="btn btn-outline-info">Submit</button></a>
                            </div>
                          </div>
                        </div>
                      </section>`
                    

  $('#formContent').append(fieldSection);
  $('input[name="fieldCount"]').val(index);

  index++;
}


$('#plus-btn').click(() => {
  addField();
})


$(document).on('click', '.bi-trash', function () {
  index--;
  $('input[name="fieldCount"]').val(index);

  $(this).closest('.field-div').remove();
  $('.field-div').each(function (index) {
    $(this).find("[name*='fieldIndex']").each(function () {
      let pre = $(this).attr("name").slice(0, 11);
      let post = $(this).attr("name").slice(12);
      $(this).attr("name", pre + index + post);
    });
  })
});
