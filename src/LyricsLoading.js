import React from 'react';

export default class LyricsLoading extends React.Component {
  render() {
    const {loading} = this.props

    if (!loading) {
      return null
    }

    return <h2>Working...</h2>
  }
}
