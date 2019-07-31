import React from 'react';

export default class LyricsForm extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      artist: props.artist,
      song: props.song,
    }
  }
  componentDidUpdate(oldProps) {
    if (oldProps.artist !== this.props.artist) {
      this.setState({artist: this.props.artist})
    }

    if (oldProps.song !== this.props.song) {
      this.setState({song: this.props.song})
    }
  }
  onSubmit(evt) {
    evt.preventDefault()

    const {artist, song} = this.state

    this.props.onSubmit(artist, song)
  }
  render() {
    const {artist, song} = this.state

    return (
      <form onSubmit={evt => this.onSubmit(evt)}>
        <div className="row">
          <input
            name="artist"
            placeholder="Enter an Artist..."
            value={artist}
            onChange={evt => this.setState({artist: evt.target.value})} />
        </div>
        <div className="row">
          <input
            name="song"
            placeholder="Search for a Song..."
            value={song}
            onChange={evt => this.setState({song: evt.target.value})} />
          <button type="submit">Search</button>
        </div>
      </form>
    );
  }
}
