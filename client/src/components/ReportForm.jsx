import React from 'react';
import Select from './Select';

function ReportTemplate() {
  return (
    <form className="report-form">
      <section>
        <fieldset>
          <legend>Used By Reporter</legend>
          <div className="grid-3">
            <Select label="Program" />

            <Select
              label="Report Type"
              options={[
                { value: '1', label: 'Coding error' },
                { value: '2', label: 'Design issue' },
                { value: '3', label: 'Suggestion' },
                { value: '4', label: 'Documentation' },
                { value: '5', label: 'Hardware' },
                { value: '6', label: 'Query' },
              ]}
            />

            <fieldset>
              <legend>Severity</legend>
              <div className="grid-3">
                <input type="radio" id="severityFatal" name="severity" />
                <label htmlFor="severityFatal">Fatal</label>

                <input type="radio" id="severitySerious" name="severity" />
                <label htmlFor="severitySerious">Serious</label>

                <input type="radio" id="severityMinor" name="severity" />
                <label htmlFor="severityMinor">Minor</label>
              </div>
            </fieldset>
          </div>

          <label>
            Problem Summary
            <input type="text" />
          </label>
          <label>
            Problem Detail
            <textarea />
          </label>

          <label htmlFor="seggestedFix">Seggested Fix (optional)</label>
          <textarea id="seggestedFix" />

          <div className="grid-2">
            <label>
              Reported By
              <input type="text" />
            </label>

            <label>
              Date
              <input type="date" />
            </label>
          </div>
        </fieldset>
      </section>

      <section>
        <fieldset>
          <legend>Used By Develop Team</legend>

          <div className="grid-2">
            <label>
              Functional Area
              <input type="text" />
            </label>

            <label>
              Assigned To
              <input type="text" />
            </label>
          </div>

          <label>
            Comments
            <textarea />
          </label>

          <div className="grid-2">
            <fieldset>
              <legend>Status</legend>
              <div className="grid-2">
                <input type="radio" id="statusOpen" name="status" />
                <label htmlFor="statusOpen">Open</label>

                <input type="radio" id="statusClosed" name="status" />
                <label htmlFor="statusClosed">Closed</label>
              </div>
            </fieldset>

            <fieldset>
              <legend>Priority</legend>
              <div className="grid-5">
                <input type="radio" id="priority1" name="priority" />
                <label htmlFor="priority1">1</label>

                <input type="radio" id="priority2" name="priority" />
                <label htmlFor="priority2">2</label>

                <input type="radio" id="priority3" name="priority" />
                <label htmlFor="priority3">3</label>

                <input type="radio" id="priority4" name="priority" />
                <label htmlFor="priority4">4</label>

                <input type="radio" id="priority5" name="priority" />
                <label htmlFor="priority5">5</label>
              </div>
            </fieldset>
          </div>
        </fieldset>
      </section>
    </form>
  );
}

export default ReportTemplate;
