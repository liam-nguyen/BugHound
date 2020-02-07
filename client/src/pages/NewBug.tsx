import React from 'react'

function NewBug() {
  return (
    <>
      <h1>New Bug Report Entry Page</h1>
      <form>
        <label>Program</label>
        <input type="text" />
        <label>Report Type</label>
        <input type="text" />
        <label>Severity</label>
        <input type="text" />
        <label>Problem Summary</label>
        <input type="text" />

        <label>Reproducible</label>
        <input type="checkbox" />

        <label>Problem</label>
        <textarea></textarea>

        <label>Suggested Fix</label>
        <textarea></textarea>

        <label>Reported By</label>
        <input type="text" />

        <label>Date</label>
        <input type="date" />

        <label>Functional Area</label>
        <input type="text" />

        <label>Assigned To</label>
        <input type="text" />

        <label>Comments</label>
        <textarea />

        <label>Status</label>
        <input type="text" />

        <label>Priority</label>
        <input type="text" />

        <label>Resolution</label>
        <input type="text" />

        <label>Resolution Version</label>
        <input type="text" />

        <label>Resolved by</label>
        <input type="text" />

        <label>Date</label>
        <input type="date" />

        <label>Treat as deferred</label>
        <input type="checkbox" />

        <button type="submit">Submit</button>
        <button type="reset">Reset</button>
        <button type="button">Cancel</button>
      </form>
    </>
  )
}

export default NewBug
