import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { increment, decrement } from './features/counter'
import { AppState } from './models'

const Counter: React.FC = () => {
  const dispatch = useDispatch()

  const count = useSelector<AppState, number>(state => state.count)

  const onClick = (): void => {
    dispatch(increment())
  }

  const dec = (): void => {
    dispatch(decrement())
  }

  return (
    <div>
      <p>{`${count}`}</p>
      <button type="button" onClick={onClick}>
        INC
      </button>

      <button type="button" onClick={dec}>
        DEC
      </button>
    </div>
  )
}

export default Counter
