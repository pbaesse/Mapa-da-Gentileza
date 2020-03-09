import React from 'react';
import { Box } from 'grommet';

const AppBar = (props) => (
  <Box
    tag='header'
    direction='row'
    align='center'
    justify='center'
    pad={{left: 'medium', right: 'small', vertical: 'small'}}
    style={{zIndex: '1'}}
    {...props}
  />
);

export default AppBar;
