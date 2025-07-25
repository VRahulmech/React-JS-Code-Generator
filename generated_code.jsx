```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import InputAdornment from '@material-ui/core/InputAdornment';
import IconButton from '@material-ui/core/IconButton';
import Visibility from '@material-ui/icons/Visibility';
import VisibilityOff from '@material-ui/icons/VisibilityOff';
import CheckCircleIcon from '@material-ui/icons/CheckCircle';
import ErrorIcon from '@material-ui/icons/Error';
import { isValidEmail } from './utils'; // Assume this utility function exists

const useStyles = makeStyles((theme) => ({
  container: {
    margin: theme.spacing(2),
    maxWidth: 400,
    width: '100%',
    padding: theme.spacing(3),
    boxShadow: theme.shadows[2],
    borderRadius: theme.shape.borderRadius,
  },
  button: {
    marginTop: theme.spacing(2),
    width: '100%',
  },
  error: {
    color: theme.palette.error.main,
  },
}));

const ValidationField = ({ isValid, ...rest }) => {
  const empty = rest.value === '';
  const valid = isValid(rest.value);
  let startAdornment;
  if (empty) {
    startAdornment = null;
  } else if (valid) {
    startAdornment = (
      <InputAdornment position="start">
        <CheckCircleIcon color="primary" />
      </InputAdornment>
    );
  } else {
    startAdornment = (
      <InputAdornment position="start">
        <ErrorIcon color="error" />
      </InputAdornment>
    );
  }
  return <TextField startAdornment={startAdornment} {...rest} />;
};

ValidationField.propTypes = {
  isValid: PropTypes.func.isRequired,
};

const LoginPage = () => {
  const classes = useStyles();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
    setError('');
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
    setError('');
  };

  const handleShowPasswordClick = () => {
    setShowPassword(!showPassword);
  };

  const handleLogin = () => {
    if (!username || !password) {
      setError('Username and password are required.');
      return;
    }
    if (!isValidEmail(username)) {
      setError('Invalid email address.');
      return;
    }
    // Simulate login logic
    console.log('Logging in:', username, password);
  };

  return (
    <Grid container justifyContent="center" alignItems="center" style={{ height: '100vh' }}>
      <Grid item>
        <div className={classes.container}>
          <ValidationField
            id="username"
            label="Username"
            type="email"
            value={username}
            onChange={handleUsernameChange}
            variant="outlined"
            margin="normal"
            fullWidth
            isValid={isValidEmail}
            error={!!error && !isValidEmail(username)}
            helperText={!!error && !isValidEmail(username) ? 'Invalid email address.' : ''}
          />
          <TextField
            id="password"
            label="Password"
            type={showPassword ? 'text' : 'password'}
            value={password}
            onChange={handlePasswordChange}
            variant="outlined"
            margin="normal"
            fullWidth
            InputProps={{
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleShowPasswordClick}
                    edge="end"
                  >
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />
          {error && <div className={classes.error}>{error}</div>}
          <Button
            variant="contained"
            color="primary"
            className={classes.button}
            onClick={handleLogin}
          >
            Sign In
          </Button>
          <Button
            variant="contained"
            color="secondary"
            className={classes.button}
            href="/signup"
          >
            Sign Up
          </Button>
          <Button
            variant="contained"
            color="secondary"
            className={classes.button}
            href="/forgot-password"
          >
            Forget Password
          </Button>
        </div>
      </Grid>
    </Grid>
  );
};

export default LoginPage;
```