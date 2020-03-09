import React from 'react';
import { Box, Button, Heading, TextInput, Anchor, Form, Grommet } from 'grommet';
import { Hide, View } from "grommet-icons";

const theme = {
  global: {
    colors: {
      brand: '#FC575E',
      background: '#FFFFFF',
      text: '#000000',
    },
    font: {
      size: '18px',
      height: '20px',
    },
  },
  button: {
    primary: {
      color: '#FC575E',
    },
    color: {
      light: '#FFFFFF',
    },
  },
};


function App() {

  const [reveal, setReveal] = React.useState(false);

  return (
    <Grommet theme={theme} full>
      <Box fill background='brand'>
        <Box direction='row' flex overflow={{horizontal: 'hidden'}}>
          <Box flex align="center" justify="center">
              <Heading color='background' margin={{left: 'medium'}}>Espalhe gentileza e amor pelo globo.</Heading>
              <Anchor color='background' alignSelf='start' margin='medium'>Saiba mais!</Anchor>
          </Box>
          <Anchor color='background' alignSelf='end' margin={{right: 'small'}} size='small'>Contribua!</Anchor>
          <Anchor color='background' alignSelf='end' margin={{right: 'small'}} size='small'>Contato</Anchor>
          <Anchor color='background' alignSelf='end' margin={{right: 'small'}} size='small'>Open Data</Anchor>
          <Box
            width='large'
            background='background'
            align='center'
            justify='center'
          >
            <Heading color='text' size='small'>Login</Heading>
            <Form>
              <Box
                width='medium'
                direction='row'
                margin='large'
                align='center'
                round='small'
                border
              >
                <TextInput plain placeholder="Email" />
              </Box>
              <Box
                width="medium"
                direction="row"
                margin="large"
                align="center"
                round="small"
                border
              >
                <TextInput
                  plain
                  placeholder="Senha"
                  type={reveal ? "text" : "password"}
                />
                <Button
                  icon={reveal ? <View size="medium" /> : <Hide size="medium" />}
                  onClick={() => setReveal(!reveal)}
                />
              </Box>
              <Button type="submit" label="Entrar" size='medium' alignSelf='center' primary />
            </Form>
          </Box>
        </Box>
      </Box>
    </Grommet>
  );
}

export default App;
