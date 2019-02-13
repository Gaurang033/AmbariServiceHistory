import React, { Component } from 'react'
import {getServiceStatus, toogleToolTipAction} from '../actions/get_service_status'
import {connect} from 'react-redux'
import StatusBar from '../components/service_bar';

class StatusBarContainer extends Component {
  render() {
    return (
        <StatusBar 
        fetchServiceStatus={this.props.fetchServiceStatus}
        service_status={this.props.service_status}
        toogleTooltip={this.props.toogleToolTip}
        toolTipOpen = {this.props.toolTipOpen}
        /> 
    )
  }
}


const mapStateToProps = state => {
  return state
}

const mapDispatchToProps = dispatch => {
  return {
    fetchServiceStatus: () => dispatch(getServiceStatus()),
    toogleToolTip: (id) => dispatch(toogleToolTipAction(id)),
    dummy: () => dispatch(toogleToolTipAction())
  }

}

export default connect(mapStateToProps, mapDispatchToProps)(StatusBarContainer)

