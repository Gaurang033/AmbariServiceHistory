import React, { Component } from 'react'
import { Tooltip } from 'reactstrap';
import './style.css'

export default class StatusBar extends Component {


    getServiceStatus = (serviceStatus, serviceName) => {
        return Object.keys(serviceStatus).map((date, index) => {
            const downTime = serviceStatus[date].downTime
            const color = downTime === 0 ?   "#36b37e" : "#bcbe2a" 
            return (
                <rect key={date} id={serviceName+'-'+ index}  height="34" width="3" x={(index + 1) * 5} y="0" fill={color} />
           )

        })
    }

    getUpTime = (serviceName) => {
        let totalDownTime = 0
        let totalTime = 0
        Object.keys(serviceName).forEach(date => {
            let dailyDownTime = serviceName[date].downTime
            let dailyTotalTime = serviceName[date].totalTime
            totalTime += dailyTotalTime;
            totalDownTime += dailyDownTime;

        })
        let totlalUptime = totalTime-totalDownTime
        return 100 * (totlalUptime / totalTime)
    }

    getLegend = (serviceName) => {
        // let upTime = this.getUpTime(serviceName)
        return (
            <div className="legend">
                <div className="legend-item">90 days ago</div>
                <div className="spacer" />
                <div className="legend-item">{this.getUpTime(serviceName)}% uptime </div>
                <div className="spacer" />
                <div className="legend-item">today</div>
            </div>


        )

    }

    getCurrentStatus = (serviceName) => {
        let currentDayStatus = serviceName[Object.keys(serviceName)[Object.keys(serviceName).length - 1]]
        let currentStatus = currentDayStatus.currentStatus

        return currentStatus === 1 ?
            <span className="component-status color-success" >Operational</span>
            : <span className="component-status color-warning" >Non-Operational</span>

    }


    componentDidMount() {
        this.props.fetchServiceStatus()
    }

    toggleToolTip = (id, event) => {
        if (event.type === "mouseout") {
            this.props.toogleTooltip(null);
          } else {
            this.props.toogleTooltip(id);
          }
    }

    getToolTip = (serviceStatus, serviceName) => {
        return Object.keys(serviceStatus).map((date, index) => {
            const downTime = serviceStatus[date].downTime
            const toolTipText = downTime === 0 ? date + "\nNo DownTime reported" : date + " Service was down for " + downTime +" minutes"

            return (
                <span key={index}>
                    <Tooltip placement="top" 
                    isOpen={this.props.toolTipOpen === serviceName + "-" + index} 
                    target={serviceName+'-'+ index} 
                    toggle={this.toggleToolTip.bind(this, serviceName + "-" + index)}>
                        {toolTipText}
                    </Tooltip>
                </span>
            )
        })
    }

    render() {
        let service_status = this.props.service_status
        return (
            service_status ?
                Object.keys(service_status).map(serviceName => {
                    return <div key={serviceName} className="component-container border-color">
                        <div className="shared-partial uptime-90-days-wrapper">
                            <span className="name"> {serviceName} </span><br />
                            {this.getCurrentStatus(service_status[serviceName])}
 
                             <svg height="34" viewBox="0 0 448 34">
                                 {this.getServiceStatus(service_status[serviceName], serviceName)}
                             </svg>
                             {this.getToolTip(service_status[serviceName], serviceName)}
                             {this.getLegend(service_status[serviceName])}
                        </div>
                    </div>

                }) : <div>Loading...</div>
        
        )
    }
}


