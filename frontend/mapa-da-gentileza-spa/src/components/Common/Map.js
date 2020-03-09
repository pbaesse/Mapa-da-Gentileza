import React, { Component, Fragment } from "react";
import ReactMapGL, { GeolocateControl } from "react-map-gl";
//import PropTypes from "prop-types";
import 'mapbox-gl/dist/mapbox-gl.css';

const TOKEN = "pk.eyJ1IjoibWF0aDc3IiwiYSI6ImNrM202NzFqdTA4bGYzY3A1ZnZvdDBhNGUifQ.T8F6GBZWX9d7Ioox41nt7g";

const geolocateStyle = {
  float: 'left',
  margin: '50px',
  padding: '10px'
};

class Map extends Component {


  state = {
    viewport: {
      width: '100%',
      height: '100%',
      latitude: -5.883912,
      longitude: -35.168858,
      zoom: 12.8
    }
  };

  componentDidMount() {
    window.onresize = () =>
      this.setState({
        viewport: {
          width: window.innerWidth,
          height: window.innerHeight,
          latitude: -5.883912,
          longitude: -35.168858,
          zoom: 12.8
        }
      });
  }


  render(){
    return(
      <Fragment>
        <ReactMapGL
          {...this.state.viewport}
          mapboxApiAccessToken={TOKEN}
          mapStyle="mapbox://styles/mapbox/outdoors-v11"
          onViewportChange={viewport => this.setState({ viewport })}
        >
        <GeolocateControl
          style={geolocateStyle}
          positionOptions={{enableHighAccuracy: true}}
          trackUserLocation={true}
        />

        </ReactMapGL>
        <button type="button" class="btn btn-primary">Primary</button>
      </Fragment>
    )
  }

}

export default Map;
