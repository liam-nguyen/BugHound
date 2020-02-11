import React from 'react';
import Select from 'react-select';

const styles = {
  control: (provided, { isFocused }) => ({
    ...provided,
    backgroundColor: isFocused ? '#d2d9dd' : '#e8eeef',
  }),
  input: provided => ({
    ...provided,
    padding: '0',
  }),
  valueContainer: provided => ({
    ...provided,
    padding: '0 8px',
  }),
};

function CustomSelect(props) {
  const { label, value, options, onChange } = props;

  return (
    <div className="select-wrapper">
      <span className="label">{label}</span>
      <Select
        styles={styles}
        value={value}
        classNamePrefix="test"
        options={options}
        onChange={onChange}
      />
    </div>
  );
}

export default CustomSelect;
