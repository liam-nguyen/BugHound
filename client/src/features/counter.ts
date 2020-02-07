import { createSlice } from '@reduxjs/toolkit'

const counterSlice = createSlice({
  name: 'count',
  initialState: 0,
  reducers: {
    increment: (state): number => state + 1,
    decrement: (state): number => state - 1,
  },
})

export const { increment, decrement } = counterSlice.actions
export default counterSlice.reducer
