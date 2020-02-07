import { combineReducers } from 'redux'
import counterReducer from '../features/counter'

const rootReducer = combineReducers({ count: counterReducer })

export default rootReducer
