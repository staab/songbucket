import React from 'react';

export default class LyricsError extends React.Component {
  render() {
    const {error} = this.props

    if (!error) {
      return null
    }

    return (
      <div>
        <h2>No Luck!</h2>
        <p>We came up empty. Try another song, or check your spelling.</p>
      </div>
    );
  }
}

